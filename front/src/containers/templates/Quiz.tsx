/* eslint-disable @typescript-eslint/no-unsafe-assignment */
import React, { FC } from 'react';
import { useQuery } from 'urql';

import gql from 'graphql-tag';
import Quiz from '../../components/templates/Quiz';

const RandomQuizsQuery = gql`
  query {
    quizByRandom {
      id
      quizId
      content
      correct
    }
  }
`;

type Response = {
  quizByRandom: {
    quizId: string;
    id: string;
    correct: boolean;
    content: string;
  }[];
};

const EnhancedQuiz: FC = () => {
  const [result] = useQuery({ query: RandomQuizsQuery });

  if (result.fetching) {
    throw new Error('Is suspense mode deactivated?');
  }
  if (result.error) {
    return <h1>{result.error.message}</h1>;
  }

  const ResponseQuiz: Response = result.data;

  return <Quiz title="Test" content={ResponseQuiz.quizByRandom[0].content} />;
};

export default EnhancedQuiz;
