import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from './App';
import UserRegister from "./components/UserRegister";
import UserLogin from "./components/UserLogin";
import MyOrders from "./components/MyOrders";

function Router() {
    return (
        <React.StrictMode>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<App /> }/>
                    <Route exact path="/users/register/" element={<UserRegister /> }/>
                    <Route exact path="/users/login/" element={<UserLogin /> }/>
                    <Route exact path="/orders/orders/" element={<MyOrders /> }/>
                </Routes>
            </BrowserRouter>
        </React.StrictMode>
    );
}


export default Router;