import nextCookie from 'next-cookies';
import Router from 'next/router';
import fetch from 'isomorphic-unfetch';

import DefaultLayout from '../../../components/layouts/default';
import { withAuthSync } from '../../../common/utils/auth';
import { LISTINGS_API_URL } from '../../../common/constants/api';


export const Listing = (props) => {
  const {listing} = props;
  return (
    <DefaultLayout>
      <h1>Listing</h1>
      <div className="row">
        <div className="images">
          <div className="image upload">
            <p>Upload a new Photo</p>
          </div>
        </div>
      </div>
      <div className="row">
        <h2>{listing.title}</h2>
        <h4>{listing.price}</h4>
        <small>{listing.location}</small>
        <p>{listing.description}</p>
      </div>
      <style jsx>{`
          .images .image {
            width: 260px;
            height: 260px;
          }
          .images .image.upload {
            border: 3px dotted #333;
            background-color: #ccc;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            text-align: center;
            align-items: center;
          }
        `}</style>
    </DefaultLayout>
  )
}

Listing.getInitialProps = async function(context) {
  const {token} = nextCookie(context);
  const {query} = context;

  const redirectOnError = () =>
    typeof window !== 'undefined'
      ? Router.push('/auth/signin')
      : context.res.writeHead(302, { Location: '/auth/signin' }).end();

  try {
    const res = await fetch(LISTINGS_API_URL(query.id), {
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        Authorization: token
      }
    });

    if (res.ok) {
      const listing = await res.json();
      return { listing };
    }
    return redirectOnError();
  } catch (error) {
    return redirectOnError();
  }
}

export default withAuthSync(Listing);
