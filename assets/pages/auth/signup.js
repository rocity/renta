import {Component} from 'react';
import DefaultLayout from '../../components/layouts/default';

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

  handleChange(e) {}
  async handleSubmit(e) {}

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
