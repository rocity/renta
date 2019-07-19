import { Component } from 'react';
import fetch from 'isomorphic-unfetch';

import DefaultLayout from '../../components/layouts/default';
import { SIGNIN_API_URL } from '../../common/constants/api';


class Signin extends Component {

  constructor(props) {
    super(props);

    this.state = {username: '', password: '', error: ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e) {
    this.setState({username: e.target.value});
  }

  async handleSubmit(e) {
    e.preventDefault();
    this.setState({error: ''});

    const username = this.state.username;
    const url = SIGNIN_API_URL();
  }

  render() {
    return (
      <DefaultLayout>
        <h1>Sign In</h1>
        <form onSubmit={this.handleSubmit}>
          <fieldset>
            <label htmlFor="username">Username</label>
            <input type="text" name="username" id="username" />
          </fieldset>
          <fieldset>
            <label htmlFor="password">Password</label>
            <input type="password" name="password" id="password" />
          </fieldset>
          <fieldset>
            <button type="submit">Sign In</button>
          </fieldset>
        </form>
      </DefaultLayout>
    )
  }
};

export default Signin;
