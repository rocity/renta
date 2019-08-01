import {Component} from 'react';
import nextCookie from 'next-cookies';
import {mapValues, get} from 'lodash';
import fetch from 'isomorphic-unfetch';

import DefaultLayout from '../../components/layouts/default';
import { LISTINGS_API_URL } from '../../common/constants/api';


class Create extends Component {
  constructor(props) {
    super(props);

    this.state = {
      form: {
        title: { value: '' },
        description: { value: '' },
        price: { value: '' },
        billing_frequency: { value: '' },
        location: { value: '' },
        location_coordinates: { value: '' }
      },
      error: {},
      success: false,
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

    const {token} = nextCookie(this);
    const url = LISTINGS_API_URL();
    const data = mapValues({...this.state.form}, i => get(i, 'value'));

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: token
        },
        body: JSON.stringify(data)
      });

      if (response.ok) {
        // Clear form
        // Show success message
        this.setState({success: true});
      } else {
        const errorJson = await response.json();

        let error = new Error(response.statusText);
        error.response = response;
        error.json = errorJson;
        throw error;
      }
    } catch (error) {
      this.setState({error: error.json});
    }
  }

  render() {
    return (
      <DefaultLayout>
        <h1>Create Listing</h1>
        <form onSubmit={this.handleSubmit}>
          <fieldset>
            <div className="row">
              <div className={"form-control " + (this.state.error.title ? 'invalid' : '')}>
                <label htmlFor="title">Title</label>
                <span className="error">{this.state.error.title}</span>
                <input
                  type="text"
                  name="title"
                  id="title"
                  value={this.state.form.title.value}
                  onChange={this.handleChange}
                />
              </div>
            </div>
            <div className="row">
              <div className={"form-control " + (this.state.error.description ? 'invalid' : '')}>
                <label htmlFor="description">Description</label>
                <span className="error">{this.state.error.description}</span>
                <textarea
                  name="description"
                  id="description"
                  rows="5"
                  value={this.state.form.description.value}
                  onChange={this.handleChange}></textarea>
              </div>
            </div>
            <div className="row">
              <div className={"form-control " + (this.state.error.price ? 'invalid' : '')}>
                <label htmlFor="price">Price</label>
                <span className="error">{this.state.error.price}</span>
                <input
                  type="number"
                  name="price"
                  id="price"
                  value={this.state.form.price.value}
                  onChange={this.handleChange}/>
              </div>
            </div>
            <div className="row">
              <div className={"form-control " + (this.state.error.billing_frequency ? 'invalid' : '')}>
                <label htmlFor="billing_frequency">Billing Frequency</label>
                <span className="error">{this.state.error.billing_frequency}</span>
                <select
                  name="billing_frequency"
                  id="billing_frequency"
                  value={this.state.form.billing_frequency.value}
                  onChange={this.handleChange}>
                  <option value="daily">Daily</option>
                  <option value="monthly">Monthly</option>
                  <option value="yearly">Yearly</option>
                </select>
              </div>
            </div>
            <div className="row">
              <div className={"form-control " + (this.state.error.location ? 'invalid' : '')}>
                <label htmlFor="location">Location</label>
                <span className="error">{this.state.error.location}</span>
                <input
                  type="text"
                  name="location"
                  id="location"
                  value={this.state.form.location.value}
                  onChange={this.handleChange}/>
              </div>
            </div>
            <div className="row">
              <div className={"form-control " + (this.state.error.location_coordinates ? 'invalid' : '')}>
                <label htmlFor="location_coordiantes">Coordinates</label>
                <span className="error">{this.state.error.location_coordiantes}</span>
                <input
                  type="text"
                  name="location_coordinates"
                  id="location_coordinates"
                  value={this.state.form.location_coordinates.value}
                  onChange={this.handleChange}/>
              </div>
            </div>
          </fieldset>
          <fieldset>
            <div className="row">
              <button type="submit">Create</button>
            </div>
          </fieldset>
        </form>

        <style jsx>{`
            form .form-control.invalid input,
            form .form-control.invalid textarea,
            form .form-control.invalid select {
              background-color: #fce4e4;
              border: 1px solid #e55039;
              outline: none;
            }
            form .form-control.invalid label {
              margin-bottom: 0;
            }
            form .form-control span.error {
              color: #e55039;
              font-size: .7em;
            }
          `}</style>
      </DefaultLayout>
    )
  }
}

export default Create;
