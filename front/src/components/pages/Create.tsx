import React, { FC } from 'react';
import 'antd/dist/antd.css';
import { Row, Typography, Card, Input, Form, Col, Button, Radio } from 'antd';
import BasicPage from '../templates/BasicPage';

const { Title } = Typography;
const { TextArea } = Input;

const Create: FC = () => (
  <BasicPage current="2">
    <Card
      title={<Title>問題を作ろう！</Title>}
      style={{
        height: 'auto',
        width: 'auto',
        margin: 'auto',
        marginBottom: 30,
        textAlign: 'center',
      }}
      loading={false}
    >
      <Row>
        <Col xs={{ span: 20, offset: 1 }} lg={{ span: 12, offset: 6 }}>
          {/* TODO: 最低6文字未満の場合はエラー出す表示にする */}
          <Form name="problem">
            <Form.Item
              label="問題文"
              hasFeedback
              help="最低６文字以上入力してください。"
              rules={[
                { required: true, message: '問題文を入力してください！' },
              ]}
            >
              <TextArea
                placeholder="（例）主キー以外は外部キー？"
                showCount
                autoSize
                allowClear
                maxLength={100}
              />
            </Form.Item>
            <Form.Item
              name="answer"
              label="答え"
              rules={[{ required: true, message: '答えを選んでね' }]}
              style={{ marginTop: 20 }}
            >
              <Radio.Group buttonStyle="solid">
                <Radio.Button value="true">True</Radio.Button>
                <Radio.Button value="false">False</Radio.Button>
              </Radio.Group>
            </Form.Item>
            <Form.Item
              label=" "
              colon={false}
              style={{ marginTop: 30 }}
              labelCol={{ span: 2 }}
            >
              <Button type="primary" htmlType="submit">
                作成
              </Button>
            </Form.Item>
          </Form>
        </Col>
      </Row>
    </Card>
  </BasicPage>
);
export default Create;
