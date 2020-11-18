import React, { FC } from 'react';
import { Layout, Typography } from 'antd';
import 'antd/dist/antd.css';

const { Header } = Layout;
const { Title } = Typography;

const SubHeader: FC = () => (
  <Header className="site-layout-sub-header-background">
    <Title style={{ textAlign: 'center', color: '#fff', margin: 10 }}>
      .Quiz
    </Title>
  </Header>
);

export default SubHeader;
