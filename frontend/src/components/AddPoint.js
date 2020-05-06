
import React, { Component } from "react";

import axios from "axios";


export default class AddPointForms extends Component{
    constructor(props) {
        super(props);
        this.state = {
            licker: '',
            lickee: '',
            point: '',
            todoList: []
        };
        this.handleChange = this.handleChange.bind(this);
    }

    mySubmitHandler = (event) => {
        console.log(this.state.lickee)
        console.log(this.state.licker)
        console.log(this.state.point)
        event.preventDefault();
        axios
            // .get("http://loyalty30.herokuapp.com/loyalty/getPoints?username=Dharmish")
            //addPoints?username=Dharmish&licker=Shivam&points=100
            .get("http://127.0.0.1:8000/loyalty/addPoints?username="+this.state.lickee+"&licker="+this.state.licker+"&points="+this.state.point)

        // alert("You are submitting " + this.state.username);
    }
    handleChange (evt) {
        // check it out: we get the evt.target.name (which will be either "email" or "password")
        // and use it to target the key on our `state` object with the same name, using bracket syntax
        this.setState({ [evt.target.name]: evt.target.value });
    }

    render() {
        return (
            <div>
            <form onSubmit={this.mySubmitHandler}>
                <label>
                    licker:
                    <input type="text" name="licker" onChange={this.handleChange}/>
                </label>
                <label>
                    lickee:
                    <input type="text" name="lickee" onChange={this.handleChange}/>
                </label>
                <label>
                    point:
                    <input type="text" name="point" onChange={this.handleChange}/>
                </label>
                <input type="submit" value="Submit" />
            </form>

            </div>
        );
    }
}