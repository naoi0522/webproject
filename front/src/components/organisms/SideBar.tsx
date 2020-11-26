import React, { FC } from 'react';
import { Layout, Menu } from 'antd';
import 'antd/dist/antd.css';

import {
  CheckCircleOutlined,
  EditOutlined,
  HomeOutlined,
  UserOutlined,
} from '@ant-design/icons';
import { Link } from 'react-router-dom';

type Props = {
  currentPage: string;
};

const { Sider } = Layout;

const SideBar: FC<Props> = ({ currentPage = '1' }) => (
  <Sider breakpoint="lg" collapsedWidth="0">
    <div className="logo" />
    <Menu theme="dark" mode="inline" defaultSelectedKeys={[currentPage]}>
      <Menu.Item key="1" icon={<HomeOutlined />}>
        <Link to="/">ホーム</Link>
      </Menu.Item>
      <Menu.Item key="2" icon={<EditOutlined />}>
        <Link to="/create">クイズを作る</Link>
      </Menu.Item>
      <Menu.Item key="3" icon={<CheckCircleOutlined />}>
        <Link to="/solve">クイズを解く</Link>
      </Menu.Item>
      <Menu.Item key="4" icon={<UserOutlined />}>
        <Link to="/users">マイページ</Link>
      </Menu.Item>
    </Menu>
  </Sider>
);

export default SideBar;
