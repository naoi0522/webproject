import React, { FC } from 'react';
import 'antd/dist/antd.css';
import BasicPage from '../templates/BasicPage';
import Quiz from '../../containers/templates/Quiz';
import './Solve.css';

const LoadingIndicator: FC = () => <h1>Loading Now</h1>;

const Solve: FC = () => (
  <BasicPage current="3">
    <React.Suspense fallback={<LoadingIndicator />}>
      <Quiz />
    </React.Suspense>
  </BasicPage>
);

export default Solve;
