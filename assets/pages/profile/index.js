import Router from 'next/router';
import fetch from 'isomorphic-unfetch';
import nextCookie from 'next-cookies';

import DefaultLayout from '../../components/layouts/default';
import { withAuthSync } from '../../common/utils/auth';
import { PROFILE_OWN_API_URL } from '../../common/constants/api';


const Profile = props => {
  const {first_name, last_name} = props;

  return (
    <div>
      <h1>Profile</h1>
      <h2>Howdy, {first_name} {last_name}!</h2>
    </div>
  )
}

Profile.getInitialProps = async function(context) {
  const {token} = nextCookie(context);

  const redirectOnError = () =>
    typeof window !== undefined
      ? Router.push('/auth/signin')
      : context.res.writeHead(302, { Location: '/auth/signin' }).end();

  try {
    const res = await fetch(PROFILE_OWN_API_URL(), {
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        Authorization: token
      }
    });

    if (res.ok) {
      return await res.json();
    }

    return redirectOnError();
  } catch (error) {
    return redirectOnError();
  }
}

export default withAuthSync(Profile);
