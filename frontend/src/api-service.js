export default class API {

    static userRegister(body) {
        return fetch(`http://127.0.0.1:8000/users/register/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body)
        }).then(resp => resp.json())
    }

    static userLogin(body) {
        return fetch(`http://127.0.0.1:8000/users/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body)
        }).then(resp => resp.json())
    }

    static getProducts() {
        return fetch(`http://127.0.0.1:8000/products/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        }).then( resp => resp.json())
    }

    static getMyOrders() {
        return fetch(`http://127.0.0.1:8000/orders/orders/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        }).then( resp => resp.json())
    }
}