import React from 'react';
import { useRef, useState, useEffect } from 'react';
import { Container, Spinner, Button } from 'react-bootstrap';
import { Row } from 'react-bootstrap';
import { Col } from 'react-bootstrap';

const FOOD_CAM = 'C922'
const PERSON_CAM = 'FaceTime'

type Result = {
  food: string,
  person: string,
  status: string,
  price: number
}

const HomePage: React.FC = () => {
  const foodRef = useRef<HTMLVideoElement | null>(null);
  const personRef = useRef<HTMLVideoElement | null>(null);

  const [transaction, setTransaction] = useState<Result | null>(null)

  navigator.mediaDevices.enumerateDevices().then(devices => {
    devices.filter(device => device.kind == "videoinput").forEach(camera => {
      navigator.mediaDevices.getUserMedia({
        video: {
          deviceId: { exact: camera.deviceId },
          width: 440,
          height: 440
        }
      }).then(stream => {
        if (camera.label.startsWith(FOOD_CAM)) {
          (foodRef.current as HTMLVideoElement).srcObject = stream;
        }
        if (camera.label.startsWith(PERSON_CAM) && personRef.current) {
          (personRef.current as HTMLVideoElement).srcObject = stream;
        }
      })
    })
  })

  const screenshot = (video: HTMLVideoElement) => {
    let w = video.videoWidth;
    let h = video.videoHeight;
    let canvas = document.createElement('canvas');
    canvas.width = w;
    canvas.height = h;
    let ctx = canvas.getContext('2d');
    if (ctx) {
      ctx.drawImage(video, 0, 0, w, h);
      return canvas.toDataURL('image/jpeg');
    }
  }

  const takeScreenshot = () => {
    let screenshots = {
      person: screenshot(personRef.current as HTMLVideoElement),
      data: screenshot(foodRef.current as HTMLVideoElement)
    };

    fetch('/dish', {
      method: 'POST',
      // mode: 'cors', // no-cors, *cors, same-origin
      // cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      // credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(screenshots)
    }).then((response) => {
      response.json().then((data: Result) => {
        if (data.food !== "background") {
          setTransaction(data)
        }
      })
    })
  }

  useEffect(() => {
    let interval: any = null;
    if (!transaction) {
      interval = setInterval(() => {
        takeScreenshot();
      }, 500);
    } else {
      clearInterval(interval);
    }
    return () => clearInterval(interval);
  }, [transaction]);

  return (
    <Container>
      <h1 className="mt-5">
        Checkout
        </h1>
      <Row className="mt-4">
        <Col sm={8}>
          <video ref={foodRef} autoPlay playsInline muted style={{ 'width': '100%' }} />
          {transaction && (
            <h2 className="text-center">
              {transaction.food} - ${transaction.price}
            </h2>
          )}
          {!transaction && (
            <h2 className="text-center">
              Food:
              <Spinner animation="grow" />
              <Spinner animation="grow" />
              <Spinner animation="grow" />
            </h2>
          )}
        </Col>

        <Col sm={4}>
          <video ref={personRef} autoPlay playsInline muted style={{ 'width': '100%' }} />
          {transaction && (
            <h1>{transaction.person}</h1>
          )}
          {!transaction && (
            <div className="text-center">
              <Spinner animation="grow" />
              <Spinner animation="grow" />
              <Spinner animation="grow" />
            </div>
          )}
          <Button variant="primary" onClick={takeScreenshot}>Screenshot</Button>
        </Col>
      </Row>
    </Container >
  )
};

export default HomePage;
