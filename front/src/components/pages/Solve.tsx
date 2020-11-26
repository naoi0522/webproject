import React, { FC } from 'react';
import { RightCircleOutlined } from '@ant-design/icons';
import 'antd/dist/antd.css';
import { Card, Typography, Radio, Button, Col, Progress } from 'antd';
import BasicPage from '../templates/BasicPage';
import './Solve.css';

const { Title, Paragraph, Text } = Typography;

const Solve: FC = () => (
  <BasicPage current="3">
    <Card
      title={<Title>第○問目</Title>}
      style={{
        height: 'auto',
        width: 'auto',
        margin: 'auto',
        marginBottom: 30,
        textAlign: 'center',
      }}
      loading={false}
    >
      <Paragraph>ここは問題文です。</Paragraph>
      <Radio.Group buttonStyle="solid">
        <Radio.Button value="true">True</Radio.Button>
        <Radio.Button value="false">False</Radio.Button>
      </Radio.Group>
      <Progress
        strokeColor={{
          '0%': '#108ee9',
          '100%': '#87d068',
        }}
        style={{ marginTop: 40 }}
        percent={10}
        status="active"
      />
    </Card>
    <Col span={6} offset={9}>
      <Button
        type="primary"
        shape="round"
        icon={<RightCircleOutlined />}
        size="large"
        block
      >
        <Text style={{ color: '#fff', fontSize: '1em' }}>次の問題へ</Text>
      </Button>
    </Col>
  </BasicPage>
);

export default Solve;
