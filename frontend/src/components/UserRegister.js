import React, {useState} from "react";
import {Form, Button, Card} from 'react-bootstrap';
import API from "../api-service";
import NavBar from "./NavBar";
import '../App.css';
import './css/Auth.css';
import { Link } from "react-router-dom";


function UserRegister() {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [first_name, setFirstName] = useState('');
    const [last_name, setLastName] = useState('');
    // const [isLogin, setIsLogin] = useState(true);


    const onClickRegister = () => {
        API.userRegister({username : username, password : password, first_name: first_name, last_name: last_name, email: email})
            .then(resp => console.log(resp))
            .catch(err => console.log(err))
    }

    return (
        <div className="App">
            <NavBar/>
            <div className="auth">
                <h2 className="text-center mb-3">Ragister</h2>
                <Card className="shadow p-3 mb-5 bg-body rounded register" style={{ width: '50rem' }}>
                    <Card.Body>
                        <Card.Title className="mb-3">Join Us And Order Your First Item</Card.Title>
                        <Form>

                            <Form.Group className="mb-3" controlId="formBasicUsername">
                                <Form.Label>Username</Form.Label>
                                <Form.Control type="text" placeholder="Username" 
                                    value={username}
                                    onChange={ event => setUsername(event.target.value)} 
                                />
                                <Form.Text className="text-muted">
                                    You have to remember this for future authentication process.
                                </Form.Text>
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formBasicPassword">
                                <Form.Label>Password</Form.Label>
                                <Form.Control type="password" placeholder="Password" 
                                    value={password}
                                    onChange={ event => setPassword(event.target.value)} 
                                />
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formBasicFirstName">
                                <Form.Label>First Name</Form.Label>
                                <Form.Control type="text" placeholder="First Name" 
                                    value={first_name}
                                    onChange={ event => setFirstName(event.target.value)} 
                                />
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formBasicLastName">
                                <Form.Label>Last Name</Form.Label>
                                <Form.Control type="text" placeholder="Last Name" 
                                    value={last_name}
                                    onChange={ event => setLastName(event.target.value)} 
                                />
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formBasicEmail">
                                <Form.Label>Email address</Form.Label>
                                <Form.Control type="email" placeholder="Enter email" 
                                    value={email}
                                    onChange={ event => setEmail(event.target.value)} 
                                />
                                <Form.Text className="text-muted">
                                We'll never share your email with anyone else.
                                </Form.Text>
                            </Form.Group>
                                <Button variant="primary" type="submit" onClick={onClickRegister}>
                                    Register
                                </Button>
                        </Form>
                        <p className="text-center mt-3">Already Have An Account? <Link to='/users/login/'>LogIn</Link></p>
                    </Card.Body>
                </Card>
            </div>
        </div>
    );
}


export default UserRegister;