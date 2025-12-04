using UnityEngine;
using RosSharp.RosBridgeClient;
using RosSharp.RosBridgeClient.MessageTypes.Std;

public class UnityRosBridge : MonoBehaviour
{
    public RosSocket rosSocket; // Assign in Inspector
    public string publisherTopic = "/unity/heartbeat";
    public string subscriberTopic = "/ros/command";
    public float publishMessageFrequency = 1f; // Hz

    private Publisher<MessageTypes.Std.String> stringPublisher;
    private MessageTypes.Std.String message;
    private float nextPublishTime = 0;

    void Start()
    {
        // Ensure RosSocket is assigned and connected
        if (rosSocket == null)
        {
            Debug.LogError("RosSocket not assigned. Please assign a RosSocket component in the Inspector.");
            enabled = false;
            return;
        }

        // Initialize publisher
        stringPublisher = new Publisher<MessageTypes.Std.String>(rosSocket, publisherTopic);
        message = new MessageTypes.Std.String();

        // Subscribe to a topic
        rosSocket.Subscribe<MessageTypes.Std.String>(subscriberTopic, ReceiveRosCommand);

        Debug.Log($"Unity-ROS Bridge started. Publishing to {publisherTopic} and subscribing to {subscriberTopic}");
    }

    void FixedUpdate()
    {
        // Publish a heartbeat message periodically
        if (Time.time >= nextPublishTime)
        {
            PublishHeartbeat();
            nextPublishTime = Time.time + 1f / publishMessageFrequency;
        }
    }

    private void PublishHeartbeat()
    {
        message.data = "Unity is alive! Current time: " + Time.time.ToString("F2");
        stringPublisher.Publish(message);
        Debug.Log($"Published: {message.data}");
    }

    private void ReceiveRosCommand(MessageTypes.Std.String rosMessage)
    {
        Debug.Log($"Received ROS command: {rosMessage.data}");
        // Here you would parse the command and control Unity elements
        // For example, if rosMessage.data == "move_forward", move a robot model.
    }

    void OnDestroy()
    {
        // Clean up subscriptions when the GameObject is destroyed
        if (rosSocket != null && rosSocket.IsConnected)
        {
            rosSocket.Unsubscribe(subscriberTopic);
        }
    }
}
