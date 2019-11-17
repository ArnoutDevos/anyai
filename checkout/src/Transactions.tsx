import React from 'react';
import { Container, Table } from 'react-bootstrap';

type Transaction = {
  name: string,
  item: string,
  price: number
}

const Transactions: React.FC = () => {
  let fromLocalStorage = localStorage.getItem('checkout_transactions')
  let transactions: Transaction[] = JSON.parse(fromLocalStorage || "[]")
  
  return (
    <Container>
      <h1 className="mt-5">Transactions</h1>
      <Table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Item</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((t, i) => (
            <tr key={i}>
              <td>{t.name}</td>
              <td>{t.item}</td>
              <td>${t.price}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Container>
  )
};

export default Transactions;
