/**
 * Add your config changes here.
 * @module config
 * @example
 * export default function applyConfig(config) {
 *   config.settings = {
 *     ...config.settings,
 *     port: 4300,
 *     listBlockTypes: {
 *       ...config.settings.listBlockTypes,
 *       'my-list-item',
 *    }
 * }
 */

// All your imports required for the config here BEFORE this line
import { BannerEdit } from '@package/components';
import { BannerView } from '@package/components';

import heroSVG from '@plone/volto/icons/hero.svg';
import '@plone/volto/config';

export default function applyConfig(config) {
  config.settings = {
    ...config.settings,
    isMultilingual: false,
    supportedLanguages: ['en'],
    defaultLanguage: 'en',
  };
  config.blocks.blocksConfig.banner = {
    id: 'banner',
    title: 'Banner',
    icon: heroSVG,
    group: 'common',
    view: BannerView,
    edit: BannerEdit,
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
  };
  return config;
}
