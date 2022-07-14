import React from 'react';
import {Table} from 'react-bootstrap';
import NavBar from './NavBar';
import './css/MyOrders.css';
import '../App.css';

function MyOrders() {
    return(
        <div className='App'>
            <NavBar />
            <div className='my-orders'>
                <h2 className='mb-5'>My Orders</h2>
                <Table striped>
                    <thead>
                        <tr>
                        <th>Id</th>
                        <th>Full Name</th>
                        <th>Phone</th>
                        <th>Cart</th>
                        <th>Price</th>
                        <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1</td>
                            <td>Mark</td>
                            <td>Otto</td>
                            <td>@mdo</td>
                        </tr>
                        <tr>
                            <td>2</td>
                            <td>Jacob</td>
                            <td>Thornton</td>
                            <td>@fat</td>
                        </tr>
                        <tr>
                            <td>3</td>
                            <td colSpan={2}>Larry the Bird</td>
                            <td>@twitter</td>
                        </tr>
                    </tbody>
                </Table>
            </div>
        </div>
    );
}


export default MyOrders;