import { Component } from 'react';
import fetch from 'isomorphic-unfetch';

import DefaultLayout from '../../components/layouts/default';
import { SIGNIN_API_URL } from '../../common/constants/api';


class Signin extends Component {

  constructor(props) {
    super(props);

    this.state = {
      form: {
        username: {value: ''},
        password: {value: ''}
      },
      error: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e) {
    const name = e.target.name;
    const value = e.target.value;

    this.setState({
      form: {
        ...this.state.form,
        [name]: {
          ...this.state.form[name],
          value
        }
      }
    });
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
            <input
              type="text"
              name="username"
              id="username"
              value={this.state.form.username.value}
              onChange={this.handleChange} />
          </fieldset>
          <fieldset>
            <label htmlFor="password">Password</label>
            <input
              type="password"
              name="password"
              id="password"
              value={this.state.form.password.value}
              onChange={this.handleChange} />
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
