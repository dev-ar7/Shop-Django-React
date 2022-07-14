import React from "react";
import '../static/css/NavBar.css';
import './css/Navbar.css';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
import {Nav} from 'react-bootstrap';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCartPlus } from '@fortawesome/free-solid-svg-icons';
// import {Link, Outlet} from 'react-router-dom';

function NavBar(props) {
        return (
            <>
                <Navbar className="shadow" collapseOnSelect expand="lg" bg="transparent" variant="transparent">
                    <Container>
                        <Navbar.Brand href="/">
                            <img src="https://cdn-icons-png.flaticon.com/512/7005/7005889.png" alt="logo" height='50' width='50'/>
                            DR Store
                        </Navbar.Brand>
                        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                        <Navbar.Collapse id="responsive-navbar-nav">
                            <Nav className="me-auto">
                                {/* <Nav.Link href="#features">Features</Nav.Link>
                                <Nav.Link href="#pricing">Pricing</Nav.Link>
                                 */}
                            </Nav>
                            <Nav className="me-5">
                                <Nav.Link href="#deets" className="mr-2 cart">
                                    <FontAwesomeIcon icon={faCartPlus}/>
                                    {/* { props.cart.length > 0 ? <b>{props.cart.length}</b> : 0} */}
                                </Nav.Link>
                                <Nav.Link href='/'>Products</Nav.Link>
                                <Nav.Link href="/orders/orders/">My Orders</Nav.Link>
                                <NavDropdown.Divider />
                                <Nav.Link href='/users/login/'>
                                    LogIn
                                </Nav.Link>
                            </Nav>
                        </Navbar.Collapse>
                    </Container>
                </Navbar>
            </>
        );
    }


export default NavBar;