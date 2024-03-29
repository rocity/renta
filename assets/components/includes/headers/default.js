import {Component} from 'react';
import Link from 'next/link';
import nextCookie from 'next-cookies';


class DefaultHeader extends Component {
  render() {
    let authLink = <Link href="/auth/signin"><a>Sign In</a></Link>;
    let registerLink = <Link href="/auth/signup"><a>Register</a></Link>;
    let createListingLink = null;

    if (this.props.isAuthed === true) {
      authLink = <Link href="/profile"><a>Profile</a></Link>;
      registerLink = null;
      createListingLink = <Link href="/listings/create"><a>Create Listing</a></Link>;
    }
    return (
      <header>
        <h2>Header</h2>
        <form>
          <fieldset>
            <input type="text" />
            <button>Search</button>
          </fieldset>
        </form>
        <ul>
          <li>
            <Link href="/"><a>Home</a></Link>
          </li>
          <li>
            <Link href="/listings"><a>Listings</a></Link>
          </li>
          <li>
            {authLink}
          </li>
          <li>
            {registerLink}
          </li>
          <li>
            {createListingLink}
          </li>
        </ul>

        <style jsx>
          {`
        li {
          display: inline;
          margin-right: 10px;
        }
        `}
        </style>
      </header>
    )
  }
}

export default DefaultHeader;
