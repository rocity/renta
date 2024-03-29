import React, { useMemo, useState } from 'react';
import nextCookie from 'next-cookies';
import Router from 'next/router';
import fetch from 'isomorphic-unfetch';
import { useDropzone } from 'react-dropzone';
import {get} from 'lodash';

import DefaultLayout from '../../../components/layouts/default';
import { withAuthSync } from '../../../common/utils/auth';
import { LISTINGS_API_URL, LISTING_IMAGES_API_URL } from '../../../common/constants/api';

const ListingImage = (props) => {
  return (
    <div>
      <div className="image">
        <img src={props.src} alt={props.alt} />
        <style jsx>{`
          .image {
            width: 260px;
            height: 260px;
            display: 'inline-block'
          }
          img {
            width: 100%;
            height: auto;
          }
        `}</style>
      </div>
    </div>
  )
}


export const Listing = (props) => {
  // Declarations
  const {listing, token} = props;
  const [files, setFiles] = useState([]);
  const [listingObj, setListingObj] = useState({});

  const dropzoneOptions = {
    accept: 'image/jpeg, image/png',
    multiple: false,
    onDrop: acceptedFiles => {
      setFiles(acceptedFiles.map(file => Object.assign(file, {
        preview: URL.createObjectURL(file)
      })));
    }
  }

  const {
    getRootProps,
    getInputProps,
    isDragActive,
    isDragAccept,
    isDragReject,
    acceptedFiles
  } = useDropzone(dropzoneOptions);

  // Events
  const handleUpload = async function (e) {
    const url = LISTING_IMAGES_API_URL();

    let data = new FormData();

    data.append('listing', listing.id);
    data.append('image', acceptedFiles[0]);

    try {
      const response = await fetch(url, {
        method: 'POST',
        body: data,
        headers: {
          Authorization: token
        }
      });
      if (response.ok) {
        const imageData = await response.json();

        // Update listing with new unage
        listing.image_urls.push(imageData);
        setListingObj(listing);

        // Reset accepted files
        setFiles([]);

        return imageData;
      }
    } catch (error) {
      // Upload error.
    }
  }

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
  let dropZoneElem = null;

  if (get(listing, 'is_owner')) {
    dropZoneElem = (
      <div {...getRootProps({ style })}>
        <input {...getInputProps()} />
        <p>Upload a new Photo</p>
      </div>
    )
  }

  if (acceptedFiles.length) {
    dropZoneElem = (
      <div>
        <ListingImage src={acceptedFiles[0].preview} alt={acceptedFiles[0].path} />
        <button onClick={handleUpload} className="button">Upload Image</button>
      </div>
    )
  }

  return (
    <DefaultLayout>
      <h1>Listing</h1>
      <div className="row">
        <div className="images">
          {dropZoneElem}
          {listing.image_urls.map(image => (
            <div className="image-wrap" key={image.id}>
              <ListingImage src={image.image} alt={image.id} />
            </div>
          ))}
        </div>
      </div>
      <div className="row">
        <h2>{listing.title}</h2>
        <small>{listing.owner}</small>
        <h4>{listing.price}</h4>
        <small>{listing.location}</small>
        <p>{listing.description}</p>
      </div>
      <style jsx>{`
        .image-wrap {
          display: inline-block;
          padding: 8px;
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
