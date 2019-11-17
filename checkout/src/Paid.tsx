import React, { useEffect } from 'react';
import { Container, Jumbotron } from 'react-bootstrap';
import { useHistory } from 'react-router-dom';

const Paid: React.FC = () => {
  let history = useHistory();
  
  useEffect(() => {
    setTimeout(() => {
      history.push('/');
    }, 3000)
  }, [history])
    
  return (
    <Container>
      <Jumbotron className="mt-5">
        <h1>Thanks for your payment, come back soon!</h1>
        <p>You'll be automatically redirected to checkout screen</p>
      </Jumbotron>
    </Container>
  )
};

export default Paid;
