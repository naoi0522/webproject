import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { BrowserRouter } from 'react-router-dom';
import {
  createClient,
  Provider,
  dedupExchange,
  cacheExchange,
  fetchExchange,
} from 'urql';
import { suspenseExchange } from '@urql/exchange-suspense';
import App from './App';

const client = createClient({
  url: 'http://localhost:5000/graphql',
  suspense: true,
  exchanges: [dedupExchange, suspenseExchange, cacheExchange, fetchExchange],
});

ReactDOM.render(
  <Provider value={client}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>,
  document.getElementById('root'),
);
