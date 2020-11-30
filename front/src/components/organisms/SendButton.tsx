import React, { FC } from 'react';
import 'antd/dist/antd.css';
import { Button } from 'antd';
import gql from 'graphql-tag';
import { useMutation } from 'urql';
import { useNavigate } from 'react-router-dom';

type Props = {
  username: string;
  password: string;
  close: VoidFunction;
};

const SendButton: FC<Props> = ({ username, password, close }) => {
  const RegisterUser = gql`
    mutation($username: String!, $password: String!) {
      createUser(input: { username: $username, password: $password }) {
        ok
      }
    }
  `;
  const [res, executeMutation] = useMutation(RegisterUser);
  const navigate = useNavigate();

  const submit = React.useCallback(async () => {
    await executeMutation({ username, password });
    localStorage.setItem('username', username);
    localStorage.setItem('password', password);
    navigate('/home');
    close();
  }, [executeMutation, username, password, close, navigate]);

  return (
    <Button disabled={res.fetching} onClick={submit} type="primary">
      Submit
    </Button>
  );
};

export default SendButton;
