import React, { FC } from 'react';
import { Route, Routes, Navigate } from 'react-router';
import Create from './components/pages/Create';
import Home from './components/pages/Home';
import Solve from './components/pages/Solve';
import Users from './components/pages/Users';

const App: FC = () => (
  <>
    {/* TODO: Routeによる画面切り替え */}
    {/* TODO: ホーム画面の実装  */}
    {/* TODO: クイズ画面の実装 */}
    {/* TODO: クイズ解答画面の実装 */}
    {/* TODO: マイページの実装 */}
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="create" element={<Create />} />
      <Route path="solve" element={<Solve />} />
      <Route path="users" element={<Users />} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  </>
);

export default App;
