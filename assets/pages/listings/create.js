import {Component} from 'react';
import nextCookie from 'next-cookies';
import DefaultLayout from '../../components/layouts/default';


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
      }
    }
    this.handleChange = this.handleChange.bind(this);
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

  render() {
    return (
      <DefaultLayout>
        <h1>Create</h1>
        <form>
          <fieldset>
            <div className="row">
              <label htmlFor="title">Title</label>
              <input
                type="text"
                name="title"
                id="title"
                value={this.state.form.title.value}
                onChange={this.handleChange}
              />
            </div>
            <div className="row">
              <label htmlFor="description">Description</label>
              <textarea
                name="description"
                id="description"
                rows="5"
                value={this.state.form.description.value}
                onChange={this.handleChange}></textarea>
            </div>
            <div className="row">
              <label htmlFor="price">Price</label>
              <input
                type="number"
                name="price"
                id="price"
                value={this.state.form.price.value}
                onChange={this.handleChange}/>
            </div>
            <div className="row">
              <label htmlFor="billing_frequency">Billing Frequency</label>
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
            <div className="row">
              <label htmlFor="location">Location</label>
              <input
                type="text"
                name="location"
                id="location"
                value={this.state.form.location.value}
                onChange={this.handleChange}/>
            </div>
            <div className="row">
              <label htmlFor="location_coordiantes">Coordinates</label>
              <input
                type="text"
                name="location_coordinates"
                id="location_coordinates"
                value={this.state.form.location_coordinates.value}
                onChange={this.handleChange}/>
            </div>
          </fieldset>
          <fieldset>
            <div className="row">
              <button type="submit">Create</button>
            </div>
          </fieldset>
        </form>
      </DefaultLayout>
    )
  }
}

// Create.getInitialProps = async function(context) {
//   const { token } = nextCookie(context);

//   const redirectOnError = () =>
//     typeof window !== 'undefined'
//       ? Router.push('/auth/signin')
//       : context.res.writeHead(302, { Location: '/auth/signin' }).end();

//   return {};
// }

export default Create;
