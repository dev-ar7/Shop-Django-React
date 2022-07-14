import React from "react";
import {Card, Button, Row, ListGroup} from 'react-bootstrap';
import '../static/css/Products.css';
import './css/Product.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faStar } from '@fortawesome/free-solid-svg-icons';


function TopRatedProds(props) {
    return (
        <div className="product-container">
                <h2>Top Rated Products</h2>
                <Row className="row">
                    { Array.isArray(props.products) && props.products.map (product => {
                        return (
                            <div>
                                { product.rating && product.rating > 4 ?
                                    <Card key={product.id} className='card' border="secondary" style={{ width: '18rem' }}>
                                        <Card.Img variant="top" src={product.image} />
                                        <Card.Body>
                                            <Card.Title>{product.name}</Card.Title>
                                            <Card.Text>
                                                {product.description}
                                            </Card.Text>
                                            <ListGroup className="list-group-flush">
                                                <ListGroup.Item>
                                                    { product.rating ? 
                                                        <b>
                                                            <FontAwesomeIcon icon={faStar} className={product.rating > 0 ? 'orange' : ''}/>
                                                            <FontAwesomeIcon icon={faStar} className={product.rating > 1 ? 'orange' : ''}/>
                                                            <FontAwesomeIcon icon={faStar} className={product.rating > 2 ? 'orange' : ''}/>
                                                            <FontAwesomeIcon icon={faStar} className={product.rating > 3 ? 'orange' : ''}/>
                                                            <FontAwesomeIcon icon={faStar} className={product.rating > 4 ? 'orange' : ''}/>
                                                            ({product.rating})
                                                        </b>
                                                        :
                                                        <p><b>No Ratins Yet</b></p>
                                                    }
                                                </ListGroup.Item>
                                                <ListGroup.Item >
                                                    <b><i>Rs. {product.price}</i></b>
                                                </ListGroup.Item>
                                            </ListGroup>
                                            <br/>
                                            <Button variant="outline-primary" >Buy Now</Button>
                                        </Card.Body>
                                    </Card>
                                :
                                ''
                                }
                            </div>
                        )
                    })}
                </Row>
            </div>
    );
}


export default TopRatedProds;