import React, { FC, useState } from 'react';
import 'antd/dist/antd.css';
import { Row, Typography, Card, Input, Form, Col, Radio } from 'antd';
import BasicPage from '../templates/BasicPage';
import QuizCreateButton from '../organisms/QuizCreateButton';

const { Title } = Typography;
const { TextArea } = Input;

const Create: FC = () => {
  const [content, setContent] = useState('');
  const [ans, setAns] = useState();

  return (
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
                  onChange={(v) => setContent(v.target.value)}
                />
              </Form.Item>
              <Form.Item
                name="answer"
                label="答え"
                rules={[{ required: true, message: '答えを選んでね' }]}
                style={{ marginTop: 20 }}
              >
                <Radio.Group
                  buttonStyle="solid"
                  onChange={(e) => setAns(e.target.value)}
                >
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
                <QuizCreateButton content={content} answer={ans} />
              </Form.Item>
            </Form>
          </Col>
        </Row>
      </Card>
    </BasicPage>
  );
};
export default Create;
