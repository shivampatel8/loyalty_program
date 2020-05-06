// frontend/src/components/Modal.js

import React, { Component } from "react";

import axios from "axios";

export default class CheckPoints extends Component{
    constructor(props) {
        super(props);
        this.state = {
            todoList:[],
            username: ''
        };
        this.handleChange = this.handleChange.bind(this);
    }

    mySubmitHandler = (event) => {
        event.preventDefault();
        axios
            .get("http://127.0.0.1:8000/loyalty/getPoints/?username="+this.state.username)
            .then(res => {


                    const myObject = JSON.parse(res.data);
                    this.setState({ todoList: myObject });
                    const items = myObject.map((item, key) =>
                        <li key={item.id}>{item.name}</li>)
                console.log(this.state.username)
                console.log(this.state.todoList)
                }
            )

    }
    handleChange (evt) {
        this.setState({ [evt.target.name]: evt.target.value });
    }
    renderItems = () => {
        const newItems = this.state.todoList
        return newItems.map(item => (

            <li
                key={item.receiver}
                className="list-group-item d-flex justify-content-between align-items-center"
            >
                {item.receiver + " " + item.points}
            </li>
        ));
    }

    render() {
        return (
            <div>
            <form onSubmit={this.mySubmitHandler}>
                <label>
                    Username:
                    <input type="text" name="username" onChange={this.handleChange}/>
                </label>
                <input type="submit" value="Submit" />
            </form>
        <ul>
            {this.renderItems()}
        </ul>
    </div>
        );
    }
}
