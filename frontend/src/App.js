import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import NavBar from './components/NavBar';
import Products from './components/Products';
import TopRatedProds from './components/TopRatedProds';
import API from './api-service';

function App() {

    const [products, setProducts] = useState([]);
    const [cart, setCart] = useState([]);

    useEffect(() => {
      API.getProducts()
          .then(resp => setProducts(resp))
          .catch(er => console.log(er))
    },[])

    const buyClicked = product => {
      setCart(product.id);
      console.log(cart);
    }

    return (
        <div className='App'>
          <NavBar 
            cart = {cart}
          />
          <Products 
            products = {products}
            buyClicked = {buyClicked}
          />
          <TopRatedProds 
            products = {products}
          />
        </div>
    );
  }

export default App;
