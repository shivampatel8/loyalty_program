 // frontend/src/App.js

    import React, { Component } from "react";
    import axios from "axios";

    class App extends Component {
      constructor(props) {
        super(props);
        this.state = {
          todoList: []
        };
      }
      // componentDidMount() {
      //   this.refreshList();
      // }
      refreshList = () => {
        axios
          // .get("http://loyalty30.herokuapp.com/loyalty/getPoints?username=Dharmish")
          .get("http://127.0.0.1:8000/loyalty/getPoints/?username=Dharmish")
          .then(res => {
                  const myObject = JSON.parse(res.data);
                  this.setState({ todoList: myObject });
                  const items = myObject.map((item, key) =>
                      <li key={item.id}>{item.name}</li>)
          }
          )
          .catch(err => console.log(err));
      };
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
      render() {
        return (
          <main className="content">
            <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
              <div id="hello">hello</div>
              <ul>
                  {this.renderItems()}
              </ul>
              <form>
                  <label>
                      Name:
                      <input type="text" name="name" />
                  </label>
                  <input type="submit" value="Submit" />
              </form>
              <button onClick={this.refreshList}>
                  Click me!
              </button>
          </main>
        );
      }
    }
    export default App;