import React, {useState} from "react";
import {Form, Button, Card} from 'react-bootstrap';
import { Link } from "react-router-dom";
import API from "../api-service";
import NavBar from "./NavBar";
import '../App.css';

function UserLogin() {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const onClickLogin = () => {
        API.userLogin( {username, password} )
            .then(resp => console.log(resp))
            .catch(err => console.log(err))
    }

    return (
        <div className="App">
            <NavBar/>
            <div className="auth">
                <h2 className="text-center mb-3">LogIn</h2>
                <Card className="shadow p-3 mb-5 bg-body rounded register" style={{ width: '50rem' }}>
                    <Card.Body>
                        <Card.Title className="mb-3">logIn To Place Your Order</Card.Title>
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
                                <Button variant="primary" type="submit" onClick={onClickLogin}>
                                    LogIn
                                </Button>
                        </Form>
                        <p className="text-center mt-3">Already Have An Account? <Link to='/users/register/'>Register</Link></p>
                    </Card.Body>
                </Card>
            </div>
        </div>
    );
}


export default UserLogin;