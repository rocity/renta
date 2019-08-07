import Link from 'next/link';
import fetch from 'isomorphic-unfetch';
import nextCookie from 'next-cookies';
import Router from 'next/router';

import DefaultLayout from '../../components/layouts/default';
import { withAuthSync } from '../../common/utils/auth';
import { LISTINGS_API_URL } from '../../common/constants/api';

const ListingLink = props => {
  const {listing} = props;
  return (
    <div>
      <div className="listing">
        <h2>
          <Link href="/listings/p/[id]" as={`/listings/p/${listing.id}`}>
            <a>{listing.title}</a>
          </Link>
        </h2>
        <small>{listing.owner}</small>
        <p>{listing.description}</p>
        <small>{listing.location}</small>
        <small>{listing.price}</small>
      </div>
      <style jsx>{`
        .listing {
          border: 1px solid #222;
          padding: 8px;

        }
        .listing h2 {
          font-size: 2em;
        }

        .listing small {
          display: block;
        }
      `}
      </style>
    </div>
  )
}

const Index = (props) => {
  return (
    <DefaultLayout>
      <h1>Listings</h1>
      <ul>
        {props.results.map(listing => (
          <li key={listing.id}>
            <ListingLink id="listing.id" listing={listing} />
          </li>
        ))}
      </ul>

      <style jsx>{`
        ul li {
          list-style: none;
        }
      `}</style>
    </DefaultLayout>
  );
}

Index.getInitialProps = async function(context) {
  const {token} = nextCookie(context);

  const redirectOnError = () =>
    typeof window !== 'undefined'
      ? Router.push('/auth/signin')
      : context.res.writeHead(302, { Location: '/auth/signin' }).end();

  try {
    const res = await fetch(LISTINGS_API_URL(), {
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

export default withAuthSync(Index);
