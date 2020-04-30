import {Component} from 'react';
import fetch from 'isomorphic-unfetch';
import { mapValues, get } from 'lodash';

import DefaultLayout from '../../components/layouts/default';
import { SIGNUP_API_URL } from '../../common/constants/api';

class SignUp extends Component {
  constructor(props) {
    super(props);

    this.state = {
      form: {
        first_name: {value: ''},
        last_name: {value: ''},
        email: {value: ''},
        password: {value: ''},
        confirm_password: {value: ''}
      },
      error: ''
    }

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

    this.setState({ error: '' });

    const url = SIGNUP_API_URL();
    const data = mapValues({ ...this.state.form }, i => get(i, 'value'));

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });

      if (response.ok) {
        // Show success message
      } else {
        const errorJson = await response.json();
        let error = new Error(response.statusText);
        error.response = response;
        error.json = errorJson;
        throw error;
      }
    } catch (error) {
      this.setState({ error: error.json });
    }
  }

  render() {
    return (
      <DefaultLayout>
        <h1>Sign Up</h1>
        <form onSubmit={this.handleSubmit}>
          <fieldset>
            <div className="row">
              <label htmlFor="first_name">Firstname</label>
              <input type="text" name="first_name" id="first_name" />
            </div>
            <div className="row">
              <label htmlFor="last_name">Lastname</label>
              <input type="text" name="last_name" id="last_name" />
            </div>
            <div className="row">
              <label htmlFor="email">Email Address</label>
              <input type="email" name="email" id="email" />
            </div>
            <div className="row">
              <label htmlFor="password">Password</label>
              <input type="password" name="password" id="password" />
            </div>
            <div className="row">
              <label htmlFor="confirm_password">Confirm Password</label>
              <input type="password" name="confirm_password" id="confirm_password" />
            </div>
          </fieldset>
          <fieldset>
            <button className="button">Sign Up</button>
          </fieldset>
        </form>
      </DefaultLayout>
    )
  }
}

export default SignUp;
