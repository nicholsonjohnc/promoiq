import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UploaderService {

  constructor(private http: HttpClient) { }
  
  uploadFile(file: any): Observable<any> {
    // curl -X POST -F 'file=@jcn.jpg' http://ec2-35-153-198-209.compute-1.amazonaws.com/v1/uploader
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'multipart/form-data'
      })
    };

    return this.http.post<any>('https://id4f29rcq8.execute-api.us-east-1.amazonaws.com/v1/uploader', file, httpOptions)
    .pipe(
      // console.log(file)
    );
  }
  
// addHero (hero: Hero): Observable<Hero> {
//   return this.http.post<Hero>(this.heroesUrl, hero, httpOptions)
//     .pipe(
//       catchError(this.handleError('addHero', hero))
//     );
// }
  
}
