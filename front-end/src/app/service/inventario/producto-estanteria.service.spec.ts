import { TestBed } from '@angular/core/testing';

import { ProductoEstanteriaService } from './producto-estanteria.service';

describe('ProductoEstanteriaService', () => {
  let service: ProductoEstanteriaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProductoEstanteriaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
