import React, { FC } from 'react';
import 'antd/dist/antd.css';
import { Card, Layout, Menu, Typography, Row, Col, Timeline } from 'antd';
import './index.css';
import { RedoOutlined } from '@ant-design/icons';
import LoginForm from '../templates/LoginForm';
import SignUpForm from '../templates/SignUpForm';

const { Header, Content, Footer } = Layout;
const { Title } = Typography;

const Index: FC = () => (
  <Layout className="layout">
    <Header>
      <div className="logo" />
      <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
        <Menu.Item key="1">
          <SignUpForm />
        </Menu.Item>
        <Menu.Item key="2">
          <LoginForm />
        </Menu.Item>
      </Menu>
    </Header>
    <Content style={{ padding: '0 50px' }}>
      <Card
        className="site-layout-content-card"
        title={<Title>クイズを解こう</Title>}
      >
        <Row>
          <Col span={6} offset={2}>
            <Timeline>
              <Timeline.Item>アカウント作成/ログイン</Timeline.Item>
              <Timeline.Item>クイズを作成</Timeline.Item>
              <Timeline.Item>クイズを解く</Timeline.Item>
              <Timeline.Item
                dot={<RedoOutlined style={{ fontSize: '16px' }} />}
              >
                繰り返し
              </Timeline.Item>
            </Timeline>
          </Col>
        </Row>
      </Card>
    </Content>
    <Footer style={{ textAlign: 'center' }}>Footer</Footer>
  </Layout>
);

export default Index;
