// 自分のユーザーID表示
// 自分が作ったクイズの情報（一覧）
// 一覧から更新と削除

import React, { FC } from 'react';
import 'antd/dist/antd.css';
import { Card, Col, Row } from 'antd';
import BasicPage from '../templates/BasicPage';

const Users: FC = () => (
  <BasicPage current="4">
    <Row>
      <Col xs={{ offset: 1, span: 22 }}>
        <Card title="user:id" style={{ height: 800, margin: 'auto' }} />
      </Col>
    </Row>
  </BasicPage>
);
export default Users;
