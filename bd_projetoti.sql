CREATE database bd_projetoti;
USS bd_projetoti;

CREATE TABLE resultados_sustentabilidade (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    consumo_agua VARCHAR(30),
    consumo_energia VARCHAR(30),
    geracao_residuos VARCHAR(30),
    residuos_reciclaveis VARCHAR(30),
    uso_transporte VARCHAR(30)
);

CREATE TABLE valores_sustentabilidade (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    valor_agua DECIMAL(9, 2),
    valor_energia DECIMAL(9, 2),
    valor_residuos DECIMAL(9, 2),
    valor_reciclaveis DECIMAL(9, 2),
    valor_transporte VARCHAR(170)
);

--INSERT INTO resultados_sustentabilidade (data, consumo_agua, consumo_energia, geracao_residuos, residuos_reciclaveis, uso_transporte) VALUES ('2025-03-24','Moderada Sustentabilidade','Alta Sustentabilidade','Alta Sustentabilidade','Baixa Sustentabilidade','Baixa Sustentabilidade');
--INSERT INTO valores_sustentabilidade (data, valor_agua, valor_energia, valor_residuos, valor_reciclaveis, valor_transporte) VALUES ('2025-03-24',100,1000,25,70,'Caminhada, Bicicleta');
--Linhas de cima apenas para testes

SELECT * FROM resultados_sustentabilidade;

SELECT
    -- Consumo de água
    CASE 
        WHEN COUNT(DISTINCT consumo_agua) = 1 AND MAX(consumo_agua) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT consumo_agua) = 1 AND MAX(consumo_agua) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_consumo_agua,

    -- Consumo de energia
    CASE 
        WHEN COUNT(DISTINCT consumo_energia) = 1 AND MAX(consumo_energia) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT consumo_energia) = 1 AND MAX(consumo_energia) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_consumo_energia,

    -- Geração de resíduos
    CASE 
        WHEN COUNT(DISTINCT geracao_residuos) = 1 AND MAX(geracao_residuos) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT geracao_residuos) = 1 AND MAX(geracao_residuos) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_geracao_residuos,

    -- Uso de transporte
    CASE 
        WHEN COUNT(DISTINCT uso_transporte) = 1 AND MAX(uso_transporte) = 'Alta Sustentabilidade' THEN 'Alta Sustentabilidade'
        WHEN COUNT(DISTINCT uso_transporte) = 1 AND MAX(uso_transporte) = 'Baixa Sustentabilidade' THEN 'Baixa Sustentabilidade'
        ELSE 'Moderada Sustentabilidade'
    END AS media_uso_transporte

FROM resultados_sustentabilidade;
