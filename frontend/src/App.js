 // frontend/src/App.js

    import React, { Component } from "react";
    import ReactDOM from 'react-dom';
    import axios from "axios";
    import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
    // import Navbar from 'react-bootstrap/Navbar'
    // import { Button, Navbar } from 'react-bootstrap'
 // import { Button, Navbar, Nav, NavItem, NavDropdown, MenuItem, Form, FormControl } from 'react-bootstrap';
    import CheckPoints from './components/Modal.js'
    import AddPointForms from './components/AddPoint.js'


    class App extends Component {
      constructor(props) {
        super(props);
        this.state = {
          todoList: [],
          username: ''
        };
      }
      // componentDidMount() {
      //   this.refreshList();
      // }
      refreshList = () => {
        axios
          // .get("http://loyalty30.herokuapp.com/loyalty/getPoints?username=Dharmish")
          .get("http://127.0.0.1:8000/loyalty/getPoints/?username="+this.state.username)
          .then(res => {
                  const myObject = JSON.parse(res.data);
                  this.setState({ todoList: myObject });
                  const items = myObject.map((item, key) =>
                      <li key={item.id}>{item.name}</li>)
          }
          )
          .catch(err => console.log(err));
      };
        mySubmitHandler = (event) => {
            event.preventDefault();
            axios
                // .get("http://loyalty30.herokuapp.com/loyalty/getPoints?username=Dharmish")
                .get("http://127.0.0.1:8000/loyalty/getPoints/?username="+this.state.username)
                .then(res => {
                        const myObject = JSON.parse(res.data);
                        this.setState({ todoList: myObject });
                        const items = myObject.map((item, key) =>
                            <li key={item.id}>{item.name}</li>)
                    }
                )
            // alert("You are submitting " + this.state.username);
        }
        myChangeHandler = (event) => {
            this.setState({username: event.target.value});
        }
        renderItems = () => {
            const newItems = this.state.todoList
            return newItems.map(item => (

                <li
                    key={item.receiver}
                    className="list-group-item d-flex justify-content-between align-items-center"
                >
                    {item.receiver+" "+item.points}
                </li>
            ));
        };
        // ReactDOM.render(<AddPointsForm />, document.getElementById('root'))
        // ReactDOM.render(<CheckPoints />, document.getElementById('root'))
      render() {
          return (
              <Router>
                  <div>
                      <h2>Welcome to React Router Tutorial</h2>
                      <nav className="navbar navbar-expand-lg navbar-light bg-light">
                          <ul className="navbar-nav mr-auto">

                              <li><Link to={'/CheckPoints'} className="nav-link">Check Points</Link></li>
                              <li><Link to={'/AddPointsForm'} className="nav-link">Add Points</Link></li>
                          </ul>
                      </nav>
                      <hr />
                      <Switch>
                          <Route exact path='/CheckPoints' component={CheckPoints} />
                          <Route exact path='/AddPointsForm' component={AddPointForms} />
                      </Switch>
                  </div>
              </Router>
          );

        // return(<Navbar bg="light" expand="lg">
        //     <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
        //     <Navbar.Toggle aria-controls="basic-navbar-nav" />
        //     <Navbar.Collapse id="basic-navbar-nav">
        //         <Nav className="mr-auto">
        //             <Nav.Link href="#home">Home</Nav.Link>
        //             <Nav.Link href="#link">Link</Nav.Link>
        //             <NavDropdown title="Dropdown" id="basic-nav-dropdown">
        //                 <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
        //                 <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
        //                 <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
        //                 <NavDropdown.Divider />
        //                 <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
        //             </NavDropdown>
        //         </Nav>
        //         <Form inline>
        //             <FormControl type="text" placeholder="Search" className="mr-sm-2" />
        //             <Button variant="outline-success">Search</Button>
        //         </Form>
        //     </Navbar.Collapse>
        // </Navbar>);
      }
    }
    export default App;