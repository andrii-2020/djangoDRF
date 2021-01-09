import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { IEmployees } from '../interfaces/employees';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EmployeesService {
  constructor(private httpClient: HttpClient) {
  }


}
