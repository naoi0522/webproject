import React, { FC } from 'react';
import 'antd/dist/antd.css';
import { Button } from 'antd';
import gql from 'graphql-tag';
import { useMutation } from 'urql';

// TODO:usernameからユーザーIDを取得するクエリを書き、
// そのユーザーIDを使ってクイズを登録し、
// ホーム画面に遷移する処理を書く

type Props = {
  content: string;
  answer: string;
};

const QuizCreateButton: FC<Props> = ({ content, answer }) => {
  const QuizCreate = gql`
    mutation($content: String!, $correct: Boolean!, $userId: Int!) {
      createQuiz(
        input: { content: $content, answer: $answer, userId: $userID }
      ) {
        ok
      }
    }
  `;
  const [res, executeMutation] = useMutation(QuizCreate);

  const submit = React.useCallback(async () => {
    await executeMutation({ content, answer });
    // TODO:
  }, [executeMutation, content, answer]);

  return (
    <Button disabled={res.fetching} onClick={submit} type="primary">
      Submit
    </Button>
  );
};

export default QuizCreateButton;
