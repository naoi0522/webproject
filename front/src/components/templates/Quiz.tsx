import React, { FC } from 'react';
import { RightCircleOutlined } from '@ant-design/icons';
import 'antd/dist/antd.css';
import { Card, Typography, Radio, Button, Col } from 'antd';

const { Title, Paragraph } = Typography;

// TODO: 内容を渡せるようにする
type Props = {
  content: string;
  title: string;
};

const Quiz: FC<Props> = ({ content, title }) => (
  <div>
    <Card
      title={<Title>{title}</Title>}
      style={{
        height: 'auto',
        width: 'auto',
        margin: 'auto',
        marginBottom: 30,
        textAlign: 'center',
      }}
      loading={false}
    >
      <Paragraph>{content}</Paragraph>
      <Radio.Group buttonStyle="solid">
        <Radio.Button value="true">True</Radio.Button>
        <Radio.Button value="false">False</Radio.Button>
      </Radio.Group>
    </Card>
    {/* TODO: 画面中央に */}
    <Col span={2} offset={11}>
      <Button
        type="primary"
        shape="round"
        icon={<RightCircleOutlined />}
        size="large"
        block
      />
    </Col>
  </div>
);

export default Quiz;
