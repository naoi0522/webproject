import React, { FC } from 'react';
import { Layout, Menu } from 'antd';
import 'antd/dist/antd.css';

import {
  CheckCircleOutlined,
  EditOutlined,
  HomeOutlined,
  UserOutlined,
} from '@ant-design/icons';

type Props = {
  currentPage: string;
};

const { Sider } = Layout;

const SideBar: FC<Props> = ({ currentPage = '1' }) => (
  <Sider breakpoint="lg" collapsedWidth="0">
    <div className="logo" />
    <Menu theme="dark" mode="inline" defaultSelectedKeys={[currentPage]}>
      <Menu.Item key="1" icon={<HomeOutlined />}>
        ホーム
      </Menu.Item>
      <Menu.Item key="2" icon={<EditOutlined />}>
        クイズを作る
      </Menu.Item>
      <Menu.Item key="3" icon={<CheckCircleOutlined />}>
        クイズを解く
      </Menu.Item>
      <Menu.Item key="4" icon={<UserOutlined />}>
        マイページ
      </Menu.Item>
    </Menu>
  </Sider>
);

export default SideBar;
