import React, { FC } from 'react';
import { Layout } from 'antd';

import './BasicPage.css';
import 'antd/dist/antd.css';
import SideBar from '../organisms/SideBar';
import SubHeader from '../organisms/SubHeader';
import SubFooter from '../organisms/SubFooter';
import Home from './Home';

const { Content } = Layout;

const BasicPage: FC = () => (
  <Layout>
    <SideBar currentPage="1" />
    <Layout>
      <SubHeader />
      <Content style={{ margin: '24px 16px 0' }}>
        <div
          className="site-layout-background"
          style={{ padding: 24, minHeight: 800 }}
        >
          {/* TODO: Routeによる画面切り替え */}
          {/* TODO:ホーム画面の実装  */}
          {/* TODO: クイズ画面の実装 */}
          {/* TODO: クイズ解答画面の実装 */}
          {/* TODO: マイページの実装 */}
          <Home />
        </div>
      </Content>

      <SubFooter />
    </Layout>
  </Layout>
);

export default BasicPage;
