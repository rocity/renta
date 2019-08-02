import React, { useMemo } from 'react';
import nextCookie from 'next-cookies';
import Router from 'next/router';
import fetch from 'isomorphic-unfetch';
import { useDropzone } from 'react-dropzone';

import DefaultLayout from '../../../components/layouts/default';
import { withAuthSync } from '../../../common/utils/auth';
import { LISTINGS_API_URL } from '../../../common/constants/api';


export const Listing = (props) => {
  const {listing} = props;
  const dropzoneOptions = {
    accept: 'image/jpeg, image/png',
    multiple: false
  }

  const {
    getRootProps,
    getInputProps,
    isDragActive,
    isDragAccept,
    isDragReject,
    acceptedFiles
  } = useDropzone(dropzoneOptions);

  const files = acceptedFiles.map(file => (
    <li key={file.path}>
      {file.path} - {file.size} bytes
    </li>
  ));

  // Dropzone Styles
  const baseStyle = {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: '20px',
    borderWidth: 2,
    borderRadius: 2,
    borderColor: '#eeeeee',
    borderStyle: 'dashed',
    backgroundColor: '#fafafa',
    color: '#bdbdbd',
    outline: 'none',
    transition: 'border .24s ease-in-out',
    width: '260px',
    height: '260px',
    justifyContent: 'center',
    flexDirection: 'column',
    textAlign: 'center',
    alignItems: 'center',
  };

  const activeStyle = {
    borderColor: '#2196f3'
  };

  const acceptStyle = {
    borderColor: '#00e676'
  };

  const rejectStyle = {
    borderColor: '#ff1744'
  };

  const style = useMemo(() => ({
    ...baseStyle,
    ...(isDragActive ? activeStyle : {}),
    ...(isDragAccept ? acceptStyle : {}),
    ...(isDragReject ? rejectStyle : {})
  }), [
      isDragActive,
      isDragReject
    ]);

  // End Dropzone Styles

  return (
    <DefaultLayout>
      <h1>Listing</h1>
      <div className="row">
        <div className="images">
          <div  {...getRootProps({style})}>
            <input {...getInputProps()} />
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
