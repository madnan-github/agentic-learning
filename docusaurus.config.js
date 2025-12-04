// @ts-check
// A complete list of Docusaurus configuration options can be found at:
// https://docusaurus.io/docs/api/docusaurus-config

const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'Teaching Physical AI and Humanoid Robotics',
  url: 'https://agentic-learning.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico', // Placeholder for now

  // GitHub pages deployment config.
  organizationName: 'agentic-learning-org',
  projectName: 'agentic-learning',

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl:
            'https://github.com/agentic-learning-org/agentic-learning/tree/main/',
        },
        blog: false, // Disable blog for now
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg', // Placeholder for now
      navbar: {
        title: 'Physical AI & Humanoid Robotics',
        logo: {
          alt: 'My Project Logo',
          src: 'img/logo.svg', // Placeholder for now
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar', // This will be defined in sidebars.js
            position: 'left',
            label: 'Book',
          },
          // You can add more navbar items here
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Book',
                to: '/docs/intro', // Link to your intro doc
              },
            ],
          },
          {
            title: 'Community',
            items: [
              // You can add community links here
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/agentic-learning-org/agentic-learning',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Agentic Learning, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: require('prism-react-renderer/themes/github'),
        darkTheme: require('prism-react-renderer/themes/dracula'),
      },
    }),
};

module.exports = config;
