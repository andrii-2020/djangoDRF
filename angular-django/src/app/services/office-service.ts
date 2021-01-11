import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {IOffices} from '../interfaces/offices';
import {Observable} from 'rxjs';
import {IEmployees} from '../interfaces/employees';

@Injectable({
  providedIn: 'root'
})
export class OfficeService {
  url = 'http://localhost:8000';

  constructor(private httpClient: HttpClient) {
  }

  getAll(): Observable<IOffices[]> {
    return this.httpClient.get<IOffices[]>(`${this.url}/offices`);
  }

  create(data: IOffices): Observable<void>{
    return this.httpClient.post<void>(`${this.url}/offices`, data);
  }

  delete(id: number): Observable<void> {
    return this.httpClient.delete<void>(`${this.url}/offices/${id}`);
  }
  getEmployees(): Observable<IEmployees[]> {
    return this.httpClient.get<IEmployees[]>('http://localhost:8000/employees');
  }

  deleteEmployees(id: number): Observable<void> {
    return this.httpClient.delete<void>(`http://localhost:8000/employees/${id}`);
  }

}
