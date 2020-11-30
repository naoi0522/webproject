import React, { FC } from 'react';
import { Route, Routes, Navigate } from 'react-router';
import Create from './components/pages/Create';
import Home from './components/pages/Home';
import Solve from './components/pages/Solve';
import Users from './components/pages/Users';
import Index from './components/pages/Index';

const App: FC = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Index />} />
        <Route path="home" element={<Home />} />
        <Route path="create" element={<Create />} />
        <Route path="solve" element={<Solve />} />
        <Route path="users" element={<Users />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </>
  );
};

export default App;
