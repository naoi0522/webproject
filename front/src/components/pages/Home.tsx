import React, { FC } from 'react';
import 'antd/dist/antd.css';
import { Card, Col, Row, Typography } from 'antd';
import BasicPage from '../templates/BasicPage';

const { Title, Paragraph } = Typography;

const Home: FC = () => (
  <BasicPage current="1">
    <Row gutter={[32, 32]}>
      <Col lg={{ span: 20, offset: 2 }} xs={{ span: 24 }}>
        <Card hoverable title={<Title level={2}>今日のクイズ</Title>}>
          <Paragraph>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Augue
            lacus viverra vitae congue eu consequat ac felis donec. Euismod in
            pellentesque massa placerat duis ultricies lacus sed turpis. Vel
            elit scelerisque mauris pellentesque pulvinar. Sed enim ut sem
            viverra aliquet.
          </Paragraph>
        </Card>
      </Col>
      <Col lg={{ span: 12 }} xs={{ span: 24 }}>
        <Card hoverable title={<Title level={2}>クイズを作る</Title>}>
          <Paragraph>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Augue
            lacus viverra vitae congue eu consequat ac felis donec. Euismod in
            pellentesque massa placerat duis ultricies lacus sed turpis. Vel
            elit scelerisque mauris pellentesque pulvinar. Sed enim ut sem
            viverra aliquet.
          </Paragraph>
        </Card>
      </Col>
      <Col lg={{ span: 12 }} xs={{ span: 24 }}>
        <Card hoverable title={<Title level={2}>クイズを解こう</Title>}>
          <Paragraph>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Augue
            lacus viverra vitae congue eu consequat ac felis donec. Euismod in
            pellentesque massa placerat duis ultricies lacus sed turpis. Vel
            elit scelerisque mauris pellentesque pulvinar. Sed enim ut sem
            viverra aliquet.
          </Paragraph>
        </Card>
      </Col>
    </Row>
  </BasicPage>
);

export default Home;
