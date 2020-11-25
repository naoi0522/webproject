import React, { FC } from 'react';
import { Layout } from 'antd';

import './BasicPage.css';
import 'antd/dist/antd.css';
import SideBar from '../organisms/SideBar';
import SubHeader from '../organisms/SubHeader';
import SubFooter from '../organisms/SubFooter';

const { Content } = Layout;

type Props = {
  current: string;
};

const BasicPage: FC<Props> = ({ current, children }) => (
  <Layout>
    <SideBar currentPage={current} />
    <Layout>
      <SubHeader />
      <Content style={{ margin: '24px 16px 0' }}>
        <div
          className="site-layout-background"
          style={{ padding: 24, minHeight: 800 }}
        >
          {children}
        </div>
      </Content>

      <SubFooter />
    </Layout>
  </Layout>
);

export default BasicPage;
